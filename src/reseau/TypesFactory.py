from src.reseau.types.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from src.reseau.types.AccountTagInformation import AccountTagInformation
from src.reseau.types.PlayerSearchCharacterNameInformation import PlayerSearchCharacterNameInformation
from src.reseau.types.PlayerSearchTagInformation import PlayerSearchTagInformation
from src.reseau.types.StatisticData import StatisticData
from src.reseau.types.StatisticDataBoolean import StatisticDataBoolean
from src.reseau.types.StatisticDataByte import StatisticDataByte
from src.reseau.types.StatisticDataInt import StatisticDataInt
from src.reseau.types.StatisticDataShort import StatisticDataShort
from src.reseau.types.StatisticDataString import StatisticDataString
from src.reseau.types.GameServerInformations import GameServerInformations
from src.reseau.types.Achievement import Achievement
from src.reseau.types.AchievementAchieved import AchievementAchieved
from src.reseau.types.AchievementAchievedRewardable import AchievementAchievedRewardable
from src.reseau.types.AchievementObjective import AchievementObjective
from src.reseau.types.AchievementStartedObjective import AchievementStartedObjective
from src.reseau.types.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from src.reseau.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect
from src.reseau.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect
from src.reseau.types.FightTemporaryBoostStateEffect import FightTemporaryBoostStateEffect
from src.reseau.types.FightTemporaryBoostWeaponDamagesEffect import FightTemporaryBoostWeaponDamagesEffect
from src.reseau.types.FightTemporarySpellBoostEffect import FightTemporarySpellBoostEffect
from src.reseau.types.FightTemporarySpellImmunityEffect import FightTemporarySpellImmunityEffect
from src.reseau.types.FightTriggeredEffect import FightTriggeredEffect
from src.reseau.types.GameActionMark import GameActionMark
from src.reseau.types.GameActionMarkedCell import GameActionMarkedCell
from src.reseau.types.ServerSessionConstant import ServerSessionConstant
from src.reseau.types.ServerSessionConstantInteger import ServerSessionConstantInteger
from src.reseau.types.ServerSessionConstantLong import ServerSessionConstantLong
from src.reseau.types.ServerSessionConstantString import ServerSessionConstantString
from src.reseau.types.AbstractCharacterInformation import AbstractCharacterInformation
from src.reseau.types.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
from src.reseau.types.CharacterMinimalAllianceInformations import CharacterMinimalAllianceInformations
from src.reseau.types.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from src.reseau.types.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations
from src.reseau.types.CharacterMinimalPlusLookAndGradeInformations import CharacterMinimalPlusLookAndGradeInformations
from src.reseau.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from src.reseau.types.ActorAlignmentInformations import ActorAlignmentInformations
from src.reseau.types.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from src.reseau.types.AlterationInfo import AlterationInfo
from src.reseau.types.CharacterCharacteristic import CharacterCharacteristic
from src.reseau.types.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from src.reseau.types.CharacterCharacteristics import CharacterCharacteristics
from src.reseau.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from src.reseau.types.CharacterCharacteristicValue import CharacterCharacteristicValue
from src.reseau.types.CharacterSpellModification import CharacterSpellModification
from src.reseau.types.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from src.reseau.types.CharacterBaseInformations import CharacterBaseInformations
from src.reseau.types.CharacterHardcoreOrEpicInformations import CharacterHardcoreOrEpicInformations
from src.reseau.types.CharacterRemodelingInformation import CharacterRemodelingInformation
from src.reseau.types.CharacterToRemodelInformations import CharacterToRemodelInformations
from src.reseau.types.RemodelingInformation import RemodelingInformation
from src.reseau.types.DebtInformation import DebtInformation
from src.reseau.types.KamaDebtInformation import KamaDebtInformation
from src.reseau.types.PlayerNote import PlayerNote
from src.reseau.types.ActorRestrictionsInformations import ActorRestrictionsInformations
from src.reseau.types.PlayerStatus import PlayerStatus
from src.reseau.types.PlayerStatusExtended import PlayerStatusExtended
from src.reseau.types.ActorOrientation import ActorOrientation
from src.reseau.types.EntityDispositionInformations import EntityDispositionInformations
from src.reseau.types.EntityMovementInformations import EntityMovementInformations
from src.reseau.types.FightEntityDispositionInformations import FightEntityDispositionInformations
from src.reseau.types.GameContextActorInformations import GameContextActorInformations
from src.reseau.types.GameContextActorPositionInformations import GameContextActorPositionInformations
from src.reseau.types.GameRolePlayTaxCollectorInformations import GameRolePlayTaxCollectorInformations
from src.reseau.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
from src.reseau.types.MapCoordinates import MapCoordinates
from src.reseau.types.MapCoordinatesAndId import MapCoordinatesAndId
from src.reseau.types.MapCoordinatesExtended import MapCoordinatesExtended
from src.reseau.types.TaxCollectorStaticExtendedInformations import TaxCollectorStaticExtendedInformations
from src.reseau.types.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from src.reseau.types.AbstractFightTeamInformations import AbstractFightTeamInformations
from src.reseau.types.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
from src.reseau.types.FightAllianceTeamInformations import FightAllianceTeamInformations
from src.reseau.types.FightCommonInformations import FightCommonInformations
from src.reseau.types.FightExternalInformations import FightExternalInformations
from src.reseau.types.FightLoot import FightLoot
from src.reseau.types.FightLootObject import FightLootObject
from src.reseau.types.FightOptionsInformations import FightOptionsInformations
from src.reseau.types.FightResultAdditionalData import FightResultAdditionalData
from src.reseau.types.FightResultExperienceData import FightResultExperienceData
from src.reseau.types.FightResultFighterListEntry import FightResultFighterListEntry
from src.reseau.types.FightResultListEntry import FightResultListEntry
from src.reseau.types.FightResultMutantListEntry import FightResultMutantListEntry
from src.reseau.types.FightResultPlayerListEntry import FightResultPlayerListEntry
from src.reseau.types.FightResultPvpData import FightResultPvpData
from src.reseau.types.FightResultTaxCollectorListEntry import FightResultTaxCollectorListEntry
from src.reseau.types.FightStartingPositions import FightStartingPositions
from src.reseau.types.FightTeamInformations import FightTeamInformations
from src.reseau.types.FightTeamLightInformations import FightTeamLightInformations
from src.reseau.types.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from src.reseau.types.FightTeamMemberEntityInformation import FightTeamMemberEntityInformation
from src.reseau.types.FightTeamMemberInformations import FightTeamMemberInformations
from src.reseau.types.FightTeamMemberMonsterInformations import FightTeamMemberMonsterInformations
from src.reseau.types.FightTeamMemberTaxCollectorInformations import FightTeamMemberTaxCollectorInformations
from src.reseau.types.FightTeamMemberWithAllianceCharacterInformations import FightTeamMemberWithAllianceCharacterInformations
from src.reseau.types.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from src.reseau.types.GameContextSummonsInformation import GameContextSummonsInformation
from src.reseau.types.GameFightAIInformations import GameFightAIInformations
from src.reseau.types.GameFightCharacterInformations import GameFightCharacterInformations
from src.reseau.types.GameFightCharacteristics import GameFightCharacteristics
from src.reseau.types.GameFightEffectTriggerCount import GameFightEffectTriggerCount
from src.reseau.types.GameFightEntityInformation import GameFightEntityInformation
from src.reseau.types.GameFightFighterEntityLightInformation import GameFightFighterEntityLightInformation
from src.reseau.types.GameFightFighterInformations import GameFightFighterInformations
from src.reseau.types.GameFightFighterLightInformations import GameFightFighterLightInformations
from src.reseau.types.GameFightFighterMonsterLightInformations import GameFightFighterMonsterLightInformations
from src.reseau.types.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from src.reseau.types.GameFightFighterNamedLightInformations import GameFightFighterNamedLightInformations
from src.reseau.types.GameFightFighterTaxCollectorLightInformations import GameFightFighterTaxCollectorLightInformations
from src.reseau.types.GameFightMonsterInformations import GameFightMonsterInformations
from src.reseau.types.GameFightMonsterWithAlignmentInformations import GameFightMonsterWithAlignmentInformations
from src.reseau.types.GameFightMutantInformations import GameFightMutantInformations
from src.reseau.types.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
from src.reseau.types.GameFightSpellCooldown import GameFightSpellCooldown
from src.reseau.types.GameFightTaxCollectorInformations import GameFightTaxCollectorInformations
from src.reseau.types.SpawnCharacterInformation import SpawnCharacterInformation
from src.reseau.types.SpawnCompanionInformation import SpawnCompanionInformation
from src.reseau.types.SpawnInformation import SpawnInformation
from src.reseau.types.SpawnMonsterInformation import SpawnMonsterInformation
from src.reseau.types.SpawnScaledMonsterInformation import SpawnScaledMonsterInformation
from src.reseau.types.AllianceInformations import AllianceInformations
from src.reseau.types.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
from src.reseau.types.AnomalySubareaInformation import AnomalySubareaInformation
from src.reseau.types.AtlasPointsInformations import AtlasPointsInformations
from src.reseau.types.BasicAllianceInformations import BasicAllianceInformations
from src.reseau.types.BasicGuildInformations import BasicGuildInformations
from src.reseau.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from src.reseau.types.GameRolePlayActorInformations import GameRolePlayActorInformations
from src.reseau.types.GameRolePlayCharacterInformations import GameRolePlayCharacterInformations
from src.reseau.types.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from src.reseau.types.GameRolePlayGroupMonsterWaveInformations import GameRolePlayGroupMonsterWaveInformations
from src.reseau.types.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from src.reseau.types.GameRolePlayMerchantInformations import GameRolePlayMerchantInformations
from src.reseau.types.GameRolePlayMountInformations import GameRolePlayMountInformations
from src.reseau.types.GameRolePlayMutantInformations import GameRolePlayMutantInformations
from src.reseau.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from src.reseau.types.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from src.reseau.types.GameRolePlayNpcWithQuestInformations import GameRolePlayNpcWithQuestInformations
from src.reseau.types.GameRolePlayPortalInformations import GameRolePlayPortalInformations
from src.reseau.types.GameRolePlayPrismInformations import GameRolePlayPrismInformations
from src.reseau.types.GameRolePlayTreasureHintInformations import GameRolePlayTreasureHintInformations
from src.reseau.types.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from src.reseau.types.GroupMonsterStaticInformationsWithAlternatives import GroupMonsterStaticInformationsWithAlternatives
from src.reseau.types.GuildInAllianceInformations import GuildInAllianceInformations
from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.HumanInformations import HumanInformations
from src.reseau.types.HumanOption import HumanOption
from src.reseau.types.HumanOptionAlliance import HumanOptionAlliance
from src.reseau.types.HumanOptionEmote import HumanOptionEmote
from src.reseau.types.HumanOptionFollowers import HumanOptionFollowers
from src.reseau.types.HumanOptionGuild import HumanOptionGuild
from src.reseau.types.HumanOptionObjectUse import HumanOptionObjectUse
from src.reseau.types.HumanOptionOrnament import HumanOptionOrnament
from src.reseau.types.HumanOptionSkillUse import HumanOptionSkillUse
from src.reseau.types.HumanOptionSpeedMultiplier import HumanOptionSpeedMultiplier
from src.reseau.types.HumanOptionTitle import HumanOptionTitle
from src.reseau.types.MonsterBoosts import MonsterBoosts
from src.reseau.types.MonsterInGroupInformations import MonsterInGroupInformations
from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from src.reseau.types.ObjectItemInRolePlay import ObjectItemInRolePlay
from src.reseau.types.AlignmentWarEffortInformation import AlignmentWarEffortInformation
from src.reseau.types.BreachBranch import BreachBranch
from src.reseau.types.BreachReward import BreachReward
from src.reseau.types.ExtendedBreachBranch import ExtendedBreachBranch
from src.reseau.types.ExtendedLockedBreachBranch import ExtendedLockedBreachBranch
from src.reseau.types.ArenaLeagueRanking import ArenaLeagueRanking
from src.reseau.types.ArenaRankInfos import ArenaRankInfos
from src.reseau.types.ArenaRanking import ArenaRanking
from src.reseau.types.LeagueFriendInformations import LeagueFriendInformations
from src.reseau.types.DecraftedItemStackInfo import DecraftedItemStackInfo
from src.reseau.types.JobBookSubscription import JobBookSubscription
from src.reseau.types.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from src.reseau.types.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from src.reseau.types.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
from src.reseau.types.JobCrafterDirectorySettings import JobCrafterDirectorySettings
from src.reseau.types.JobDescription import JobDescription
from src.reseau.types.JobExperience import JobExperience
from src.reseau.types.MapNpcQuestInfo import MapNpcQuestInfo
from src.reseau.types.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
from src.reseau.types.NamedPartyTeam import NamedPartyTeam
from src.reseau.types.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
from src.reseau.types.PartyGuestInformations import PartyGuestInformations
from src.reseau.types.PartyInvitationMemberInformations import PartyInvitationMemberInformations
from src.reseau.types.PartyMemberArenaInformations import PartyMemberArenaInformations
from src.reseau.types.PartyMemberGeoPosition import PartyMemberGeoPosition
from src.reseau.types.PartyMemberInformations import PartyMemberInformations
from src.reseau.types.PartyEntityBaseInformation import PartyEntityBaseInformation
from src.reseau.types.PartyEntityMemberInformation import PartyEntityMemberInformation
from src.reseau.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
from src.reseau.types.QuestActiveDetailedInformations import QuestActiveDetailedInformations
from src.reseau.types.QuestActiveInformations import QuestActiveInformations
from src.reseau.types.QuestObjectiveInformations import QuestObjectiveInformations
from src.reseau.types.QuestObjectiveInformationsWithCompletion import QuestObjectiveInformationsWithCompletion
from src.reseau.types.PortalInformation import PortalInformation
from src.reseau.types.TreasureHuntFlag import TreasureHuntFlag
from src.reseau.types.TreasureHuntStep import TreasureHuntStep
from src.reseau.types.TreasureHuntStepDig import TreasureHuntStepDig
from src.reseau.types.TreasureHuntStepFight import TreasureHuntStepFight
from src.reseau.types.TreasureHuntStepFollowDirection import TreasureHuntStepFollowDirection
from src.reseau.types.TreasureHuntStepFollowDirectionToHint import TreasureHuntStepFollowDirectionToHint
from src.reseau.types.TreasureHuntStepFollowDirectionToPOI import TreasureHuntStepFollowDirectionToPOI
from src.reseau.types.BidExchangerObjectInfo import BidExchangerObjectInfo
from src.reseau.types.ForgettableSpellItem import ForgettableSpellItem
from src.reseau.types.GoldItem import GoldItem
from src.reseau.types.Item import Item
from src.reseau.types.ObjectEffects import ObjectEffects
from src.reseau.types.ObjectItem import ObjectItem
from src.reseau.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from src.reseau.types.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity
from src.reseau.types.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from src.reseau.types.ObjectItemNotInContainer import ObjectItemNotInContainer
from src.reseau.types.ObjectItemQuantity import ObjectItemQuantity
from src.reseau.types.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from src.reseau.types.ObjectItemToSell import ObjectItemToSell
from src.reseau.types.ObjectItemToSellInBid import ObjectItemToSellInBid
from src.reseau.types.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop
from src.reseau.types.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop
from src.reseau.types.SellerBuyerDescriptor import SellerBuyerDescriptor
from src.reseau.types.SpellItem import SpellItem
from src.reseau.types.ObjectEffect import ObjectEffect
from src.reseau.types.ObjectEffectCreature import ObjectEffectCreature
from src.reseau.types.ObjectEffectDate import ObjectEffectDate
from src.reseau.types.ObjectEffectDice import ObjectEffectDice
from src.reseau.types.ObjectEffectDuration import ObjectEffectDuration
from src.reseau.types.ObjectEffectInteger import ObjectEffectInteger
from src.reseau.types.ObjectEffectLadder import ObjectEffectLadder
from src.reseau.types.ObjectEffectMinMax import ObjectEffectMinMax
from src.reseau.types.ObjectEffectMount import ObjectEffectMount
from src.reseau.types.ObjectEffectString import ObjectEffectString
from src.reseau.types.EntityInformation import EntityInformation
from src.reseau.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from src.reseau.types.FinishMoveInformations import FinishMoveInformations
from src.reseau.types.AbstractContactInformations import AbstractContactInformations
from src.reseau.types.AcquaintanceInformation import AcquaintanceInformation
from src.reseau.types.AcquaintanceOnlineInformation import AcquaintanceOnlineInformation
from src.reseau.types.FriendInformations import FriendInformations
from src.reseau.types.FriendOnlineInformations import FriendOnlineInformations
from src.reseau.types.FriendSpouseInformations import FriendSpouseInformations
from src.reseau.types.FriendSpouseOnlineInformations import FriendSpouseOnlineInformations
from src.reseau.types.IgnoredInformations import IgnoredInformations
from src.reseau.types.IgnoredOnlineInformations import IgnoredOnlineInformations
from src.reseau.types.Contribution import Contribution
from src.reseau.types.GuildEmblem import GuildEmblem
from src.reseau.types.GuildMember import GuildMember
from src.reseau.types.GuildRankInformation import GuildRankInformation
from src.reseau.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from src.reseau.types.GuildRankPublicInformation import GuildRankPublicInformation
from src.reseau.types.HavenBagFurnitureInformation import HavenBagFurnitureInformation
from src.reseau.types.ApplicationPlayerInformation import ApplicationPlayerInformation
from src.reseau.types.GuildApplicationInformation import GuildApplicationInformation
from src.reseau.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from src.reseau.types.GuildLogbookChestActivity import GuildLogbookChestActivity
from src.reseau.types.GuildLevelUpActivity import GuildLevelUpActivity
from src.reseau.types.GuildPaddockActivity import GuildPaddockActivity
from src.reseau.types.GuildPlayerFlowActivity import GuildPlayerFlowActivity
from src.reseau.types.GuildPlayerRankUpdateActivity import GuildPlayerRankUpdateActivity
from src.reseau.types.GuildRankActivity import GuildRankActivity
from src.reseau.types.GuildUnlockNewTabActivity import GuildUnlockNewTabActivity
from src.reseau.types.GuildRecruitmentInformation import GuildRecruitmentInformation
from src.reseau.types.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from src.reseau.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from src.reseau.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from src.reseau.types.TaxCollectorFightersInformation import TaxCollectorFightersInformation
from src.reseau.types.TaxCollectorGuildInformations import TaxCollectorGuildInformations
from src.reseau.types.TaxCollectorInformations import TaxCollectorInformations
from src.reseau.types.TaxCollectorLootInformations import TaxCollectorLootInformations
from src.reseau.types.TaxCollectorMovement import TaxCollectorMovement
from src.reseau.types.TaxCollectorWaitingForHelpInformations import TaxCollectorWaitingForHelpInformations
from src.reseau.types.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
from src.reseau.types.AccountHouseInformations import AccountHouseInformations
from src.reseau.types.HouseGuildedInformations import HouseGuildedInformations
from src.reseau.types.HouseInformations import HouseInformations
from src.reseau.types.HouseInformationsForGuild import HouseInformationsForGuild
from src.reseau.types.HouseInformationsForSell import HouseInformationsForSell
from src.reseau.types.HouseInformationsInside import HouseInformationsInside
from src.reseau.types.HouseInstanceInformations import HouseInstanceInformations
from src.reseau.types.HouseOnMapInformations import HouseOnMapInformations
from src.reseau.types.Idol import Idol
from src.reseau.types.PartyIdol import PartyIdol
from src.reseau.types.InteractiveElement import InteractiveElement
from src.reseau.types.InteractiveElementNamedSkill import InteractiveElementNamedSkill
from src.reseau.types.InteractiveElementSkill import InteractiveElementSkill
from src.reseau.types.InteractiveElementWithAgeBonus import InteractiveElementWithAgeBonus
from src.reseau.types.MapObstacle import MapObstacle
from src.reseau.types.StatedElement import StatedElement
from src.reseau.types.SkillActionDescription import SkillActionDescription
from src.reseau.types.SkillActionDescriptionCollect import SkillActionDescriptionCollect
from src.reseau.types.SkillActionDescriptionCraft import SkillActionDescriptionCraft
from src.reseau.types.SkillActionDescriptionTimed import SkillActionDescriptionTimed
from src.reseau.types.TeleportDestination import TeleportDestination
from src.reseau.types.StorageTabInformation import StorageTabInformation
from src.reseau.types.UpdatedStorageTabInformation import UpdatedStorageTabInformation
from src.reseau.types.RecycledItem import RecycledItem
from src.reseau.types.EntityLook import EntityLook
from src.reseau.types.IndexedEntityLook import IndexedEntityLook
from src.reseau.types.SubEntity import SubEntity
from src.reseau.types.ItemDurability import ItemDurability
from src.reseau.types.MountClientData import MountClientData
from src.reseau.types.UpdateMountBooleanCharacteristic import UpdateMountBooleanCharacteristic
from src.reseau.types.UpdateMountCharacteristic import UpdateMountCharacteristic
from src.reseau.types.UpdateMountIntegerCharacteristic import UpdateMountIntegerCharacteristic
from src.reseau.types.MountInformationsForPaddock import MountInformationsForPaddock
from src.reseau.types.PaddockBuyableInformations import PaddockBuyableInformations
from src.reseau.types.PaddockContentInformations import PaddockContentInformations
from src.reseau.types.PaddockGuildedInformations import PaddockGuildedInformations
from src.reseau.types.PaddockInformations import PaddockInformations
from src.reseau.types.PaddockInformationsForSell import PaddockInformationsForSell
from src.reseau.types.PaddockInstancesInformations import PaddockInstancesInformations
from src.reseau.types.PaddockItem import PaddockItem
from src.reseau.types.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
from src.reseau.types.EntitiesPreset import EntitiesPreset
from src.reseau.types.ForgettableSpellsPreset import ForgettableSpellsPreset
from src.reseau.types.FullStatsPreset import FullStatsPreset
from src.reseau.types.IconNamedPreset import IconNamedPreset
from src.reseau.types.IdolsPreset import IdolsPreset
from src.reseau.types.ItemForPreset import ItemForPreset
from src.reseau.types.ItemsPreset import ItemsPreset
from src.reseau.types.Preset import Preset
from src.reseau.types.PresetsContainerPreset import PresetsContainerPreset
from src.reseau.types.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
from src.reseau.types.SpellForPreset import SpellForPreset
from src.reseau.types.SpellsPreset import SpellsPreset
from src.reseau.types.StatsPreset import StatsPreset
from src.reseau.types.AllianceInsiderPrismInformation import AllianceInsiderPrismInformation
from src.reseau.types.AlliancePrismInformation import AlliancePrismInformation
from src.reseau.types.PrismFightersInformation import PrismFightersInformation
from src.reseau.types.PrismGeolocalizedInformation import PrismGeolocalizedInformation
from src.reseau.types.PrismInformation import PrismInformation
from src.reseau.types.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from src.reseau.types.Shortcut import Shortcut
from src.reseau.types.ShortcutEmote import ShortcutEmote
from src.reseau.types.ShortcutEntitiesPreset import ShortcutEntitiesPreset
from src.reseau.types.ShortcutObject import ShortcutObject
from src.reseau.types.ShortcutObjectIdolsPreset import ShortcutObjectIdolsPreset
from src.reseau.types.ShortcutObjectItem import ShortcutObjectItem
from src.reseau.types.ShortcutObjectPreset import ShortcutObjectPreset
from src.reseau.types.ShortcutSmiley import ShortcutSmiley
from src.reseau.types.ShortcutSpell import ShortcutSpell
from src.reseau.types.AbstractSocialGroupInfos import AbstractSocialGroupInfos
from src.reseau.types.AlliancedGuildFactSheetInformations import AlliancedGuildFactSheetInformations
from src.reseau.types.AllianceFactSheetInformations import AllianceFactSheetInformations
from src.reseau.types.GuildFactSheetInformations import GuildFactSheetInformations
from src.reseau.types.GuildInAllianceVersatileInformations import GuildInAllianceVersatileInformations
from src.reseau.types.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from src.reseau.types.GuildVersatileInformations import GuildVersatileInformations
from src.reseau.types.StartupActionAddObject import StartupActionAddObject
from src.reseau.types.TrustCertificate import TrustCertificate
from src.reseau.types.Version import Version
from src.reseau.types.BufferInformation import BufferInformation
class TypesFactory:
    id_class = {
    "1941": AbstractPlayerSearchInformation,
    "3843": AccountTagInformation,
    "2582": PlayerSearchCharacterNameInformation,
    "9354": PlayerSearchTagInformation,
    "9976": StatisticData,
    "1668": StatisticDataBoolean,
    "6014": StatisticDataByte,
    "5020": StatisticDataInt,
    "4566": StatisticDataShort,
    "3754": StatisticDataString,
    "8236": GameServerInformations,
    "8605": Achievement,
    "3784": AchievementAchieved,
    "3393": AchievementAchievedRewardable,
    "6520": AchievementObjective,
    "1412": AchievementStartedObjective,
    "5809": FightDispellableEffectExtendedInformations,
    "2930": AbstractFightDispellableEffect,
    "9498": FightTemporaryBoostEffect,
    "1699": FightTemporaryBoostStateEffect,
    "320": FightTemporaryBoostWeaponDamagesEffect,
    "2068": FightTemporarySpellBoostEffect,
    "3005": FightTemporarySpellImmunityEffect,
    "9782": FightTriggeredEffect,
    "9955": GameActionMark,
    "322": GameActionMarkedCell,
    "1655": ServerSessionConstant,
    "6759": ServerSessionConstantInteger,
    "7150": ServerSessionConstantLong,
    "1087": ServerSessionConstantString,
    "7583": AbstractCharacterInformation,
    "9408": CharacterBasicMinimalInformations,
    "3044": CharacterMinimalAllianceInformations,
    "6596": CharacterMinimalGuildInformations,
    "3491": CharacterMinimalGuildPublicInformations,
    "1826": CharacterMinimalInformations,
    "1566": CharacterMinimalPlusLookAndGradeInformations,
    "5553": CharacterMinimalPlusLookInformations,
    "1359": ActorAlignmentInformations,
    "7208": ActorExtendedAlignmentInformations,
    "1321": AlterationInfo,
    "1975": CharacterCharacteristic,
    "4320": CharacterCharacteristicDetailed,
    "3763": CharacterCharacteristics,
    "9594": CharacterCharacteristicsInformations,
    "9": CharacterCharacteristicValue,
    "5928": CharacterSpellModification,
    "8115": CharacterUsableCharacteristicDetailed,
    "5241": CharacterBaseInformations,
    "4055": CharacterHardcoreOrEpicInformations,
    "497": CharacterRemodelingInformation,
    "3766": CharacterToRemodelInformations,
    "5883": RemodelingInformation,
    "2197": DebtInformation,
    "5100": KamaDebtInformation,
    "5149": PlayerNote,
    "9952": ActorRestrictionsInformations,
    "2800": PlayerStatus,
    "6689": PlayerStatusExtended,
    "7032": ActorOrientation,
    "4639": EntityDispositionInformations,
    "6656": EntityMovementInformations,
    "1045": FightEntityDispositionInformations,
    "2731": GameContextActorInformations,
    "5791": GameContextActorPositionInformations,
    "3371": GameRolePlayTaxCollectorInformations,
    "4115": IdentifiedEntityDispositionInformations,
    "3296": MapCoordinates,
    "8277": MapCoordinatesAndId,
    "6443": MapCoordinatesExtended,
    "3048": TaxCollectorStaticExtendedInformations,
    "4251": TaxCollectorStaticInformations,
    "2288": AbstractFightTeamInformations,
    "7820": BaseSpawnMonsterInformation,
    "6485": FightAllianceTeamInformations,
    "5016": FightCommonInformations,
    "907": FightExternalInformations,
    "4171": FightLoot,
    "6606": FightLootObject,
    "7533": FightOptionsInformations,
    "7465": FightResultAdditionalData,
    "4352": FightResultExperienceData,
    "9670": FightResultFighterListEntry,
    "652": FightResultListEntry,
    "2534": FightResultMutantListEntry,
    "4199": FightResultPlayerListEntry,
    "6318": FightResultPvpData,
    "9330": FightResultTaxCollectorListEntry,
    "5329": FightStartingPositions,
    "1598": FightTeamInformations,
    "567": FightTeamLightInformations,
    "3454": FightTeamMemberCharacterInformations,
    "3734": FightTeamMemberEntityInformation,
    "4449": FightTeamMemberInformations,
    "7483": FightTeamMemberMonsterInformations,
    "3317": FightTeamMemberTaxCollectorInformations,
    "3981": FightTeamMemberWithAllianceCharacterInformations,
    "5258": GameContextBasicSpawnInformation,
    "4966": GameContextSummonsInformation,
    "8962": GameFightAIInformations,
    "5869": GameFightCharacterInformations,
    "9003": GameFightCharacteristics,
    "9447": GameFightEffectTriggerCount,
    "9037": GameFightEntityInformation,
    "125": GameFightFighterEntityLightInformation,
    "1336": GameFightFighterInformations,
    "8097": GameFightFighterLightInformations,
    "622": GameFightFighterMonsterLightInformations,
    "2626": GameFightFighterNamedInformations,
    "7812": GameFightFighterNamedLightInformations,
    "5273": GameFightFighterTaxCollectorLightInformations,
    "7996": GameFightMonsterInformations,
    "685": GameFightMonsterWithAlignmentInformations,
    "5304": GameFightMutantInformations,
    "8179": GameFightResumeSlaveInfo,
    "457": GameFightSpellCooldown,
    "6160": GameFightTaxCollectorInformations,
    "8127": SpawnCharacterInformation,
    "5290": SpawnCompanionInformation,
    "4164": SpawnInformation,
    "4683": SpawnMonsterInformation,
    "4208": SpawnScaledMonsterInformation,
    "7721": AllianceInformations,
    "7939": AlternativeMonstersInGroupLightInformations,
    "4282": AnomalySubareaInformation,
    "8332": AtlasPointsInformations,
    "8784": BasicAllianceInformations,
    "9708": BasicGuildInformations,
    "5831": BasicNamedAllianceInformations,
    "5525": GameRolePlayActorInformations,
    "5128": GameRolePlayCharacterInformations,
    "163": GameRolePlayGroupMonsterInformations,
    "4916": GameRolePlayGroupMonsterWaveInformations,
    "9573": GameRolePlayHumanoidInformations,
    "8878": GameRolePlayMerchantInformations,
    "3397": GameRolePlayMountInformations,
    "9024": GameRolePlayMutantInformations,
    "6078": GameRolePlayNamedActorInformations,
    "8667": GameRolePlayNpcInformations,
    "4530": GameRolePlayNpcWithQuestInformations,
    "4492": GameRolePlayPortalInformations,
    "1935": GameRolePlayPrismInformations,
    "944": GameRolePlayTreasureHintInformations,
    "7530": GroupMonsterStaticInformations,
    "4706": GroupMonsterStaticInformationsWithAlternatives,
    "4097": GuildInAllianceInformations,
    "9043": GuildInformations,
    "3552": HumanInformations,
    "9012": HumanOption,
    "4905": HumanOptionAlliance,
    "9108": HumanOptionEmote,
    "2344": HumanOptionFollowers,
    "9583": HumanOptionGuild,
    "9917": HumanOptionObjectUse,
    "2913": HumanOptionOrnament,
    "7124": HumanOptionSkillUse,
    "7522": HumanOptionSpeedMultiplier,
    "5285": HumanOptionTitle,
    "207": MonsterBoosts,
    "6852": MonsterInGroupInformations,
    "9510": MonsterInGroupLightInformations,
    "7895": ObjectItemInRolePlay,
    "1780": AlignmentWarEffortInformation,
    "4093": BreachBranch,
    "9610": BreachReward,
    "2411": ExtendedBreachBranch,
    "3360": ExtendedLockedBreachBranch,
    "7018": ArenaLeagueRanking,
    "7486": ArenaRankInfos,
    "8576": ArenaRanking,
    "895": LeagueFriendInformations,
    "461": DecraftedItemStackInfo,
    "8668": JobBookSubscription,
    "1457": JobCrafterDirectoryEntryJobInfo,
    "5518": JobCrafterDirectoryEntryPlayerInfo,
    "3210": JobCrafterDirectoryListEntry,
    "8707": JobCrafterDirectorySettings,
    "4832": JobDescription,
    "4673": JobExperience,
    "8165": MapNpcQuestInfo,
    "1089": DungeonPartyFinderPlayer,
    "8137": NamedPartyTeam,
    "4353": NamedPartyTeamWithOutcome,
    "302": PartyGuestInformations,
    "1462": PartyInvitationMemberInformations,
    "7745": PartyMemberArenaInformations,
    "3347": PartyMemberGeoPosition,
    "2562": PartyMemberInformations,
    "6238": PartyEntityBaseInformation,
    "2153": PartyEntityMemberInformation,
    "2902": GameRolePlayNpcQuestFlag,
    "1711": QuestActiveDetailedInformations,
    "7467": QuestActiveInformations,
    "7608": QuestObjectiveInformations,
    "8445": QuestObjectiveInformationsWithCompletion,
    "7576": PortalInformation,
    "242": TreasureHuntFlag,
    "1380": TreasureHuntStep,
    "3158": TreasureHuntStepDig,
    "2025": TreasureHuntStepFight,
    "6206": TreasureHuntStepFollowDirection,
    "1280": TreasureHuntStepFollowDirectionToHint,
    "3670": TreasureHuntStepFollowDirectionToPOI,
    "8070": BidExchangerObjectInfo,
    "9195": ForgettableSpellItem,
    "2227": GoldItem,
    "454": Item,
    "983": ObjectEffects,
    "4970": ObjectItem,
    "664": ObjectItemGenericQuantity,
    "2112": ObjectItemInformationWithQuantity,
    "9973": ObjectItemMinimalInformation,
    "9381": ObjectItemNotInContainer,
    "9156": ObjectItemQuantity,
    "1796": ObjectItemQuantityPriceDateEffects,
    "1640": ObjectItemToSell,
    "7697": ObjectItemToSellInBid,
    "2396": ObjectItemToSellInHumanVendorShop,
    "7129": ObjectItemToSellInNpcShop,
    "2285": SellerBuyerDescriptor,
    "1609": SpellItem,
    "3919": ObjectEffect,
    "9687": ObjectEffectCreature,
    "1929": ObjectEffectDate,
    "7888": ObjectEffectDice,
    "1728": ObjectEffectDuration,
    "5629": ObjectEffectInteger,
    "3891": ObjectEffectLadder,
    "8222": ObjectEffectMinMax,
    "6010": ObjectEffectMount,
    "3289": ObjectEffectString,
    "2982": EntityInformation,
    "1177": ProtectedEntityWaitingForHelpInfo,
    "5507": FinishMoveInformations,
    "6748": AbstractContactInformations,
    "8682": AcquaintanceInformation,
    "7790": AcquaintanceOnlineInformation,
    "6377": FriendInformations,
    "9867": FriendOnlineInformations,
    "9427": FriendSpouseInformations,
    "385": FriendSpouseOnlineInformations,
    "9376": IgnoredInformations,
    "911": IgnoredOnlineInformations,
    "5925": Contribution,
    "1463": GuildEmblem,
    "8142": GuildMember,
    "1327": GuildRankInformation,
    "4985": GuildRankMinimalInformation,
    "4081": GuildRankPublicInformation,
    "2126": HavenBagFurnitureInformation,
    "3215": ApplicationPlayerInformation,
    "9865": GuildApplicationInformation,
    "9885": GuildLogbookEntryBasicInformation,
    "4972": GuildLogbookChestActivity,
    "6657": GuildLevelUpActivity,
    "1038": GuildPaddockActivity,
    "784": GuildPlayerFlowActivity,
    "2477": GuildPlayerRankUpdateActivity,
    "6210": GuildRankActivity,
    "1415": GuildUnlockNewTabActivity,
    "9554": GuildRecruitmentInformation,
    "8796": AdditionalTaxCollectorInformations,
    "2455": TaxCollectorBasicInformations,
    "1761": TaxCollectorComplementaryInformations,
    "6077": TaxCollectorFightersInformation,
    "3945": TaxCollectorGuildInformations,
    "1698": TaxCollectorInformations,
    "31": TaxCollectorLootInformations,
    "3370": TaxCollectorMovement,
    "5219": TaxCollectorWaitingForHelpInformations,
    "7547": HavenBagRoomPreviewInformation,
    "4255": AccountHouseInformations,
    "5826": HouseGuildedInformations,
    "8100": HouseInformations,
    "6571": HouseInformationsForGuild,
    "17": HouseInformationsForSell,
    "3735": HouseInformationsInside,
    "3939": HouseInstanceInformations,
    "2212": HouseOnMapInformations,
    "5898": Idol,
    "2232": PartyIdol,
    "6827": InteractiveElement,
    "8158": InteractiveElementNamedSkill,
    "6496": InteractiveElementSkill,
    "7257": InteractiveElementWithAgeBonus,
    "8540": MapObstacle,
    "528": StatedElement,
    "2974": SkillActionDescription,
    "4182": SkillActionDescriptionCollect,
    "8945": SkillActionDescriptionCraft,
    "8684": SkillActionDescriptionTimed,
    "1363": TeleportDestination,
    "8868": StorageTabInformation,
    "3407": UpdatedStorageTabInformation,
    "3983": RecycledItem,
    "792": EntityLook,
    "5822": IndexedEntityLook,
    "8172": SubEntity,
    "6797": ItemDurability,
    "5415": MountClientData,
    "3282": UpdateMountBooleanCharacteristic,
    "3174": UpdateMountCharacteristic,
    "9909": UpdateMountIntegerCharacteristic,
    "6920": MountInformationsForPaddock,
    "6796": PaddockBuyableInformations,
    "4925": PaddockContentInformations,
    "1561": PaddockGuildedInformations,
    "2730": PaddockInformations,
    "2038": PaddockInformationsForSell,
    "3870": PaddockInstancesInformations,
    "7524": PaddockItem,
    "7978": CharacterCharacteristicForPreset,
    "7302": EntitiesPreset,
    "6946": ForgettableSpellsPreset,
    "6627": FullStatsPreset,
    "9579": IconNamedPreset,
    "4104": IdolsPreset,
    "3034": ItemForPreset,
    "5609": ItemsPreset,
    "7679": Preset,
    "3018": PresetsContainerPreset,
    "9479": SimpleCharacterCharacteristicForPreset,
    "4357": SpellForPreset,
    "4946": SpellsPreset,
    "6299": StatsPreset,
    "4596": AllianceInsiderPrismInformation,
    "1085": AlliancePrismInformation,
    "3512": PrismFightersInformation,
    "8286": PrismGeolocalizedInformation,
    "7553": PrismInformation,
    "323": PrismSubareaEmptyInfo,
    "5639": Shortcut,
    "9965": ShortcutEmote,
    "3958": ShortcutEntitiesPreset,
    "6067": ShortcutObject,
    "472": ShortcutObjectIdolsPreset,
    "954": ShortcutObjectItem,
    "7026": ShortcutObjectPreset,
    "8390": ShortcutSmiley,
    "2349": ShortcutSpell,
    "7197": AbstractSocialGroupInfos,
    "6222": AlliancedGuildFactSheetInformations,
    "883": AllianceFactSheetInformations,
    "9855": GuildFactSheetInformations,
    "7435": GuildInAllianceVersatileInformations,
    "8297": GuildInsiderFactSheetInformations,
    "2866": GuildVersatileInformations,
    "5455": StartupActionAddObject,
    "1235": TrustCertificate,
    "6891": Version,
    "1204": BufferInformation
    }
    
    @classmethod
    def get_instance_id(cls,id,content):
        return cls.id_class[str(id)](content)
    