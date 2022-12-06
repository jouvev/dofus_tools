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
    "5286": AbstractPlayerSearchInformation,
    "4213": AccountTagInformation,
    "4980": PlayerSearchCharacterNameInformation,
    "8414": PlayerSearchTagInformation,
    "9676": StatisticData,
    "2517": StatisticDataBoolean,
    "8126": StatisticDataByte,
    "8260": StatisticDataInt,
    "603": StatisticDataShort,
    "6817": StatisticDataString,
    "2762": GameServerInformations,
    "7432": Achievement,
    "3063": AchievementAchieved,
    "2637": AchievementAchievedRewardable,
    "4324": AchievementObjective,
    "6750": AchievementStartedObjective,
    "5136": FightDispellableEffectExtendedInformations,
    "7598": AbstractFightDispellableEffect,
    "1595": FightTemporaryBoostEffect,
    "8812": FightTemporaryBoostStateEffect,
    "9808": FightTemporaryBoostWeaponDamagesEffect,
    "1274": FightTemporarySpellBoostEffect,
    "5875": FightTemporarySpellImmunityEffect,
    "5276": FightTriggeredEffect,
    "7942": GameActionMark,
    "1423": GameActionMarkedCell,
    "9098": ServerSessionConstant,
    "9099": ServerSessionConstantInteger,
    "1486": ServerSessionConstantLong,
    "8495": ServerSessionConstantString,
    "7441": AbstractCharacterInformation,
    "467": CharacterBasicMinimalInformations,
    "9153": CharacterMinimalAllianceInformations,
    "6211": CharacterMinimalGuildInformations,
    "9695": CharacterMinimalGuildPublicInformations,
    "2938": CharacterMinimalInformations,
    "9686": CharacterMinimalPlusLookAndGradeInformations,
    "5838": CharacterMinimalPlusLookInformations,
    "1577": ActorAlignmentInformations,
    "7183": ActorExtendedAlignmentInformations,
    "7259": AlterationInfo,
    "3999": CharacterCharacteristic,
    "3932": CharacterCharacteristicDetailed,
    "9878": CharacterCharacteristics,
    "9105": CharacterCharacteristicsInformations,
    "6375": CharacterCharacteristicValue,
    "2905": CharacterSpellModification,
    "9660": CharacterUsableCharacteristicDetailed,
    "3972": CharacterBaseInformations,
    "5965": CharacterHardcoreOrEpicInformations,
    "3502": CharacterRemodelingInformation,
    "6791": CharacterToRemodelInformations,
    "5693": RemodelingInformation,
    "2854": DebtInformation,
    "1295": KamaDebtInformation,
    "7031": PlayerNote,
    "231": ActorRestrictionsInformations,
    "6409": PlayerStatus,
    "2424": PlayerStatusExtended,
    "8265": ActorOrientation,
    "6822": EntityDispositionInformations,
    "1071": EntityMovementInformations,
    "1876": FightEntityDispositionInformations,
    "6154": GameContextActorInformations,
    "4353": GameContextActorPositionInformations,
    "7265": GameRolePlayTaxCollectorInformations,
    "6158": IdentifiedEntityDispositionInformations,
    "434": MapCoordinates,
    "9300": MapCoordinatesAndId,
    "892": MapCoordinatesExtended,
    "2929": TaxCollectorStaticExtendedInformations,
    "4346": TaxCollectorStaticInformations,
    "7551": AbstractFightTeamInformations,
    "523": BaseSpawnMonsterInformation,
    "3124": FightAllianceTeamInformations,
    "7540": FightCommonInformations,
    "4041": FightExternalInformations,
    "6118": FightLoot,
    "1928": FightLootObject,
    "3516": FightOptionsInformations,
    "2387": FightResultAdditionalData,
    "3399": FightResultExperienceData,
    "8547": FightResultFighterListEntry,
    "676": FightResultListEntry,
    "7849": FightResultMutantListEntry,
    "9016": FightResultPlayerListEntry,
    "5866": FightResultPvpData,
    "1141": FightResultTaxCollectorListEntry,
    "9514": FightStartingPositions,
    "9665": FightTeamInformations,
    "4037": FightTeamLightInformations,
    "9478": FightTeamMemberCharacterInformations,
    "3000": FightTeamMemberEntityInformation,
    "8044": FightTeamMemberInformations,
    "622": FightTeamMemberMonsterInformations,
    "8225": FightTeamMemberTaxCollectorInformations,
    "1608": FightTeamMemberWithAllianceCharacterInformations,
    "9317": GameContextBasicSpawnInformation,
    "1691": GameContextSummonsInformation,
    "5338": GameFightAIInformations,
    "8256": GameFightCharacterInformations,
    "709": GameFightCharacteristics,
    "6210": GameFightEffectTriggerCount,
    "2308": GameFightEntityInformation,
    "9520": GameFightFighterEntityLightInformation,
    "8667": GameFightFighterInformations,
    "1381": GameFightFighterLightInformations,
    "6010": GameFightFighterMonsterLightInformations,
    "6988": GameFightFighterNamedInformations,
    "4228": GameFightFighterNamedLightInformations,
    "3187": GameFightFighterTaxCollectorLightInformations,
    "5931": GameFightMonsterInformations,
    "5161": GameFightMonsterWithAlignmentInformations,
    "5030": GameFightMutantInformations,
    "149": GameFightResumeSlaveInfo,
    "6738": GameFightSpellCooldown,
    "7033": GameFightTaxCollectorInformations,
    "4647": SpawnCharacterInformation,
    "2297": SpawnCompanionInformation,
    "7132": SpawnInformation,
    "9613": SpawnMonsterInformation,
    "5733": SpawnScaledMonsterInformation,
    "1445": AllianceInformations,
    "9311": AlternativeMonstersInGroupLightInformations,
    "753": AnomalySubareaInformation,
    "8644": AtlasPointsInformations,
    "2850": BasicAllianceInformations,
    "3099": BasicGuildInformations,
    "1895": BasicNamedAllianceInformations,
    "6893": GameRolePlayActorInformations,
    "9999": GameRolePlayCharacterInformations,
    "5208": GameRolePlayGroupMonsterInformations,
    "8577": GameRolePlayGroupMonsterWaveInformations,
    "2890": GameRolePlayHumanoidInformations,
    "3744": GameRolePlayMerchantInformations,
    "4593": GameRolePlayMountInformations,
    "3361": GameRolePlayMutantInformations,
    "4532": GameRolePlayNamedActorInformations,
    "1079": GameRolePlayNpcInformations,
    "7406": GameRolePlayNpcWithQuestInformations,
    "7029": GameRolePlayPortalInformations,
    "2910": GameRolePlayPrismInformations,
    "2825": GameRolePlayTreasureHintInformations,
    "2259": GroupMonsterStaticInformations,
    "6494": GroupMonsterStaticInformationsWithAlternatives,
    "2149": GuildInAllianceInformations,
    "5879": GuildInformations,
    "4254": HumanInformations,
    "7895": HumanOption,
    "6815": HumanOptionAlliance,
    "7493": HumanOptionEmote,
    "5290": HumanOptionFollowers,
    "1317": HumanOptionGuild,
    "4121": HumanOptionObjectUse,
    "9052": HumanOptionOrnament,
    "1413": HumanOptionSkillUse,
    "5081": HumanOptionSpeedMultiplier,
    "8686": HumanOptionTitle,
    "6611": MonsterBoosts,
    "4170": MonsterInGroupInformations,
    "7887": MonsterInGroupLightInformations,
    "7139": ObjectItemInRolePlay,
    "9859": AlignmentWarEffortInformation,
    "4023": BreachBranch,
    "1621": BreachReward,
    "2200": ExtendedBreachBranch,
    "7105": ExtendedLockedBreachBranch,
    "4388": ArenaLeagueRanking,
    "9362": ArenaRankInfos,
    "5644": ArenaRanking,
    "8986": LeagueFriendInformations,
    "1657": DecraftedItemStackInfo,
    "1331": JobBookSubscription,
    "2848": JobCrafterDirectoryEntryJobInfo,
    "8918": JobCrafterDirectoryEntryPlayerInfo,
    "2555": JobCrafterDirectoryListEntry,
    "9680": JobCrafterDirectorySettings,
    "6046": JobDescription,
    "4639": JobExperience,
    "1379": MapNpcQuestInfo,
    "3739": DungeonPartyFinderPlayer,
    "1488": NamedPartyTeam,
    "4812": NamedPartyTeamWithOutcome,
    "1801": PartyGuestInformations,
    "7042": PartyInvitationMemberInformations,
    "5619": PartyMemberArenaInformations,
    "1033": PartyMemberGeoPosition,
    "2681": PartyMemberInformations,
    "1277": PartyEntityBaseInformation,
    "6691": PartyEntityMemberInformation,
    "2213": GameRolePlayNpcQuestFlag,
    "5482": QuestActiveDetailedInformations,
    "883": QuestActiveInformations,
    "3887": QuestObjectiveInformations,
    "765": QuestObjectiveInformationsWithCompletion,
    "9720": PortalInformation,
    "1394": TreasureHuntFlag,
    "9826": TreasureHuntStep,
    "6207": TreasureHuntStepDig,
    "832": TreasureHuntStepFight,
    "3809": TreasureHuntStepFollowDirection,
    "4635": TreasureHuntStepFollowDirectionToHint,
    "5302": TreasureHuntStepFollowDirectionToPOI,
    "9027": BidExchangerObjectInfo,
    "650": ForgettableSpellItem,
    "7613": GoldItem,
    "2394": Item,
    "3634": ObjectEffects,
    "122": ObjectItem,
    "3048": ObjectItemGenericQuantity,
    "3982": ObjectItemInformationWithQuantity,
    "7239": ObjectItemMinimalInformation,
    "9268": ObjectItemNotInContainer,
    "8102": ObjectItemQuantity,
    "2847": ObjectItemQuantityPriceDateEffects,
    "4449": ObjectItemToSell,
    "1881": ObjectItemToSellInBid,
    "8803": ObjectItemToSellInHumanVendorShop,
    "3715": ObjectItemToSellInNpcShop,
    "708": SellerBuyerDescriptor,
    "2784": SpellItem,
    "2375": ObjectEffect,
    "2792": ObjectEffectCreature,
    "1793": ObjectEffectDate,
    "9849": ObjectEffectDice,
    "5181": ObjectEffectDuration,
    "5142": ObjectEffectInteger,
    "9939": ObjectEffectLadder,
    "8669": ObjectEffectMinMax,
    "2066": ObjectEffectMount,
    "4073": ObjectEffectString,
    "7875": EntityInformation,
    "9095": ProtectedEntityWaitingForHelpInfo,
    "5282": FinishMoveInformations,
    "2855": AbstractContactInformations,
    "6961": AcquaintanceInformation,
    "9922": AcquaintanceOnlineInformation,
    "5744": FriendInformations,
    "1113": FriendOnlineInformations,
    "1698": FriendSpouseInformations,
    "1090": FriendSpouseOnlineInformations,
    "3964": IgnoredInformations,
    "277": IgnoredOnlineInformations,
    "5831": Contribution,
    "6191": GuildEmblem,
    "4700": GuildMember,
    "8982": GuildRankInformation,
    "9298": GuildRankMinimalInformation,
    "8341": GuildRankPublicInformation,
    "1499": HavenBagFurnitureInformation,
    "7768": ApplicationPlayerInformation,
    "8441": GuildApplicationInformation,
    "9953": GuildLogbookEntryBasicInformation,
    "9668": GuildLogbookChestActivity,
    "118": GuildLevelUpActivity,
    "2307": GuildPaddockActivity,
    "3798": GuildPlayerFlowActivity,
    "9810": GuildPlayerRankUpdateActivity,
    "3613": GuildRankActivity,
    "7590": GuildUnlockNewTabActivity,
    "1049": GuildRecruitmentInformation,
    "5519": AdditionalTaxCollectorInformations,
    "8484": TaxCollectorBasicInformations,
    "4404": TaxCollectorComplementaryInformations,
    "755": TaxCollectorFightersInformation,
    "3219": TaxCollectorGuildInformations,
    "2087": TaxCollectorInformations,
    "3251": TaxCollectorLootInformations,
    "7076": TaxCollectorMovement,
    "5562": TaxCollectorWaitingForHelpInformations,
    "4008": HavenBagRoomPreviewInformation,
    "8301": AccountHouseInformations,
    "8503": HouseGuildedInformations,
    "5804": HouseInformations,
    "4778": HouseInformationsForGuild,
    "2248": HouseInformationsForSell,
    "5325": HouseInformationsInside,
    "5383": HouseInstanceInformations,
    "7324": HouseOnMapInformations,
    "1259": Idol,
    "8979": PartyIdol,
    "7572": InteractiveElement,
    "7491": InteractiveElementNamedSkill,
    "9259": InteractiveElementSkill,
    "2757": InteractiveElementWithAgeBonus,
    "9250": MapObstacle,
    "3190": StatedElement,
    "2029": SkillActionDescription,
    "6936": SkillActionDescriptionCollect,
    "1139": SkillActionDescriptionCraft,
    "4372": SkillActionDescriptionTimed,
    "9417": TeleportDestination,
    "9635": StorageTabInformation,
    "4597": UpdatedStorageTabInformation,
    "3353": RecycledItem,
    "343": EntityLook,
    "1690": IndexedEntityLook,
    "2388": SubEntity,
    "2028": ItemDurability,
    "1985": MountClientData,
    "1498": UpdateMountBooleanCharacteristic,
    "9715": UpdateMountCharacteristic,
    "3041": UpdateMountIntegerCharacteristic,
    "8850": MountInformationsForPaddock,
    "1961": PaddockBuyableInformations,
    "9501": PaddockContentInformations,
    "1931": PaddockGuildedInformations,
    "8948": PaddockInformations,
    "5760": PaddockInformationsForSell,
    "2666": PaddockInstancesInformations,
    "1199": PaddockItem,
    "8283": CharacterCharacteristicForPreset,
    "6291": EntitiesPreset,
    "2189": ForgettableSpellsPreset,
    "8548": FullStatsPreset,
    "5740": IconNamedPreset,
    "9110": IdolsPreset,
    "3514": ItemForPreset,
    "8763": ItemsPreset,
    "4929": Preset,
    "5978": PresetsContainerPreset,
    "8099": SimpleCharacterCharacteristicForPreset,
    "6944": SpellForPreset,
    "7557": SpellsPreset,
    "7648": StatsPreset,
    "5890": AllianceInsiderPrismInformation,
    "8324": AlliancePrismInformation,
    "1824": PrismFightersInformation,
    "8423": PrismGeolocalizedInformation,
    "1566": PrismInformation,
    "2190": PrismSubareaEmptyInfo,
    "3762": Shortcut,
    "6747": ShortcutEmote,
    "8093": ShortcutEntitiesPreset,
    "3305": ShortcutObject,
    "9778": ShortcutObjectIdolsPreset,
    "1320": ShortcutObjectItem,
    "7965": ShortcutObjectPreset,
    "5066": ShortcutSmiley,
    "8571": ShortcutSpell,
    "7462": AbstractSocialGroupInfos,
    "4861": AlliancedGuildFactSheetInformations,
    "3583": AllianceFactSheetInformations,
    "558": GuildFactSheetInformations,
    "5353": GuildInAllianceVersatileInformations,
    "487": GuildInsiderFactSheetInformations,
    "1609": GuildVersatileInformations,
    "9542": StartupActionAddObject,
    "429": TrustCertificate,
    "2462": Version,
    "6969": BufferInformation
    }
    
    @classmethod
    def get_instance_id(cls,id,content):
        return cls.id_class[str(id)](content)
    